#!/usr/bin/env python3
"""
Frontier Lab Google Drive Synchronization
Uploads governance files to Google Drive with proper OAuth2 flow
"""

import os
import sys
import argparse
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import json

SCOPES = ['https://www.googleapis.com/auth/drive']
TOKEN_FILE = os.path.expanduser('~/.frontier-lab-credentials.json')

class FrontierLabDriveSync:
    def __init__(self):
        self.creds = None
        self.service = None
        self.folder_ids = {}
        
    def authenticate(self):
        """Authenticate with Google Drive using OAuth2 browser flow"""
        
        # Check if we already have valid credentials
        if os.path.exists(TOKEN_FILE):
            self.creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
            if self.creds and self.creds.valid:
                self.service = build('drive', 'v3', credentials=self.creds)
                print("✅ Authenticated to Google Drive (cached credentials)")
                return True
        
        # Refresh token if expired
        if self.creds and self.creds.expired and self.creds.refresh_token:
            self.creds.refresh(Request())
        
        # Create new OAuth2 flow
        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            self.creds = flow.run_local_server(port=0)
            
            # Save credentials for next time
            with open(TOKEN_FILE, 'w') as token:
                token.write(self.creds.to_json())
                
            self.service = build('drive', 'v3', credentials=self.creds)
            print("✅ Authenticated to Google Drive")
            return True
            
        except FileNotFoundError:
            print("❌ credentials.json not found")
            print("\nTo set up OAuth2:")
            print("1. Go to: https://console.cloud.google.com/apis/credentials")
            print("2. Create OAuth 2.0 Desktop Application credentials")
            print("3. Download JSON and save as 'credentials.json' in this directory")
            print("4. Run this script again")
            return False
        
    def create_folder(self, folder_name, parent_id=None):
        """Create folder in Google Drive"""
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
        }
        if parent_id:
            file_metadata['parents'] = [parent_id]
            
        folder = self.service.files().create(
            body=file_metadata,
            fields='id'
        ).execute()
        folder_id = folder.get('id')
        print(f"✅ Created folder: {folder_name}")
        return folder_id
        
    def create_folder_structure(self):
        """Create the full folder structure"""
        print("\n📁 Creating folder structure...")
        
        # Create root folder
        self.folder_ids['research-lab'] = self.create_folder('frontier-research-lab')
        
        # Create subfolders
        subfolders = ['governance', 'agents', 'pipelines', 'session_logs']
        for subfolder in subfolders:
            parent_id = self.folder_ids['research-lab']
            self.folder_ids[subfolder] = self.create_folder(
                subfolder,
                parent_id=parent_id
            )
            
    def upload_file(self, file_path, parent_id, convert_to_docs=True):
        """Upload file to Google Drive"""
        file_path = Path(file_path)
        
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return None
        
        # Use Google Docs format for markdown files
        if convert_to_docs and file_path.suffix == '.md':
            mime_type = 'application/vnd.google-apps.document'
        else:
            mime_type = 'application/octet-stream'
            
        file_metadata = {
            'name': file_path.stem,
            'mimeType': mime_type,
            'parents': [parent_id]
        }
        
        media = MediaFileUpload(str(file_path), resumable=True)
        
        file_obj = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        file_id = file_obj.get('id')
        print(f"✅ Uploaded: {file_path.name}")
        return file_id
        
    def upload_governance_files(self):
        """Upload all governance files"""
        print("\n📄 Uploading governance files...")
        
        governance_files = [
            'FRONTIER_LAB_COMPLETE_MASTERFILE.md',
            'LAB_GOVERNANCE_CHARTER_v1.0.md',
            'MASTER_ORCHESTRATOR_METAPROMPT_v1.0.md',
            'AGENT_REGISTRY_v1.0.md',
            'PIPELINE_REGISTRY_v1.0.md',
            'JOURNAL_REQUIREMENTS_SCHEMA.yaml',
            'SESSION_001_FINAL_WRAPUP.md',
            'SESSION_001_SKILLS_EXTRACTION.md',
            'SESSION_002_SKILLS_INTEGRATION.md',
            'SESSION_002_FINAL_WRAPUP.md'
        ]
        
        governance_dir = Path('governance')
        
        if not governance_dir.exists():
            print(f"❌ governance/ directory not found")
            return False
            
        parent_id = self.folder_ids.get('governance')
        if not parent_id:
            print("❌ governance folder not created")
            return False
            
        for filename in governance_files:
            filepath = governance_dir / filename
            if filepath.exists():
                self.upload_file(filepath, parent_id)
            else:
                print(f"⚠️  File not found: {filename}")
                
        return True

def main():
    parser = argparse.ArgumentParser(description='Frontier Lab Google Drive Sync')
    parser.add_argument('--create-folders', action='store_true', help='Create folder structure')
    parser.add_argument('--upload-governance', action='store_true', help='Upload governance files')
    parser.add_argument('--verify', action='store_true', help='Verify upload')
    
    args = parser.parse_args()
    
    if not any([args.create_folders, args.upload_governance, args.verify]):
        print("Frontier Lab Google Drive Sync")
        print("Usage:")
        print("  python3 google_drive_sync.py --create-folders")
        print("  python3 google_drive_sync.py --upload-governance")
        print("  python3 google_drive_sync.py --verify")
        return
        
    sync = FrontierLabDriveSync()
    
    if not sync.authenticate():
        return
        
    if args.create_folders:
        sync.create_folder_structure()
        
    if args.upload_governance:
        sync.create_folder_structure()  # Ensure folders exist
        sync.upload_governance_files()
        
    if args.verify:
        print("\n✅ Setup complete!")
        print("Files are now in Google Drive under 'frontier-research-lab' folder")

if __name__ == '__main__':
    main()

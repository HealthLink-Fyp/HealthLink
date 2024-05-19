import { CallService } from 'src/app/architecture/services/call/call.service';

import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { TranscribeService } from 'src/app/architecture/services/call/transcribe.service';
import { SharedService } from 'src/app/architecture/services/shared.service';
import { CaptureImgService } from 'src/app/architecture/services/emotions/capture-img.service';

@Component({
  selector: 'app-dialog',
  templateUrl: './dialog.component.html',
  styleUrls: ['./dialog.component.css']
})

export class DialogComponent {
  text: string | undefined;

  constructor(
      public dialogRef: MatDialogRef<DialogComponent>,
      @Inject(MAT_DIALOG_DATA) public data: DialogData,
      private _snackBar: MatSnackBar, 
      public service : TranscribeService,
      private CallService:CallService,
      private keyService:SharedService,
      private imageCaptureService: CaptureImgService
  ) {
     
  this.service.init()
   }

   

   ngOnInit(): void {
    this.CallService.peerIdGet().subscribe((response:any)=>{
      console.log("i m getting the peer id in dialog component")
      this.data.peerId = response.peer_id; // Set the initial value of the input field to the peerId value
      this.imageCaptureService.startImageCapture();
    })
   

    
  }

  
public startService(){

  // this.service.start()

}


  public showCopiedSnackBar() {   
  
       
      this._snackBar.open('Peer ID Copied!', 'Hurrah', {
      duration: 1000,
      horizontalPosition: 'center',
      verticalPosition: 'top'
    });

  }
}

export interface DialogData {
  peerId?: string;
  joinCall: boolean
}




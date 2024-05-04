import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class NotifyService {

  constructor(private snackBar:MatSnackBar) { }

  showSuccess(message:string)
  {
    this.snackBar.open(message,'close',{
      duration:60000,
      panelClass:['mdc-snackbar__surface','success'],
      verticalPosition: 'top', // Add this line
      horizontalPosition: 'end', // Set to 'end' to align right
    })
  }

  showError(message:string)
  {
    this.snackBar.open(message,'close',{
      duration:60000,
      panelClass:['mdc-snackbar__surface','error'],
      verticalPosition: 'top', // Add this line
      horizontalPosition: 'end', // Set to 'end' to align right
    })
  }

  showWarning(message:string)
  {
    this.snackBar.open(message,'close',{
      duration:60000,
      panelClass:['mdc-snackbar__surface','warning'],
      verticalPosition: 'top', // Add this line
      horizontalPosition: 'end', // Set to 'end' to align right
    })
  }

  showPending(message:string)
  {
    this.snackBar.open(message,'close',{
      duration:60000,
      panelClass:['mdc-snackbar__surface','pending'],
      verticalPosition: 'top', // Add this line
      horizontalPosition: 'end', // Set to 'end' to align right
    })
  }
}

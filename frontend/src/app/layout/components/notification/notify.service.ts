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
      panelClass:['mdc-snackbar__surface','success']
    })
  }

  showError(message:string)
  {
    this.snackBar.open(message,'close',{
      duration:60000,
      panelClass:['mdc-snackbar__surface','error']
    })
  }

  showWarning(message:string)
  {
    this.snackBar.open(message,'close',{
      duration:60000,
      panelClass:['mdc-snackbar__surface','warning']
    })
  }

  showPending(message:string)
  {
    this.snackBar.open(message,'close',{
      duration:60000,
      panelClass:['mdc-snackbar__surface','pending']
    })
  }
}

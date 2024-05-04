import { Component } from '@angular/core';
import { NotifyService } from './notify.service';

@Component({
  selector: 'app-notification',
  templateUrl: './notification.component.html',
  styleUrls: ['./notification.component.css']
})
export class NotificationComponent {
  constructor(private notifyService:NotifyService){}

  showSuccess()
  {
    this.notifyService.showSuccess('This is a success message');
  }

  showError()
  {
    this.notifyService.showError('This is an error message');
  }

  showWarning()
  {
    this.notifyService.showWarning('This is a warning message');
  }

  showPending()
  {
    this.notifyService.showPending('This is a pending notification');
  }
}

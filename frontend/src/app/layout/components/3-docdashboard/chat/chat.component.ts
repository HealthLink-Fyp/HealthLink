import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs/operators';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';
import { environment } from 'src/environment/environment';

@Component({
  selector: 'app-chat1',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {

  ngOnInit(): void {
   
    
  }

 
  savePatId(patId: any) {
    console.log('Book Appointment clicked for ID:', patId);
    this.pat_id=patId;
    this.createWebSocketConnection();
  }

  tokeny:any=''

  createWebSocketConnection() {
    const token = localStorage.getItem('token');
    this.tokeny=token;
    this.chatSocket = new WebSocket(`${environment.testApi}/${this.pat_id}/?token= ${token}`);
   console.log()

    this.chatSocket.onopen = (e) => {
      console.log('Chat socket successfully connected.');
    };

    this.chatSocket.onclose = (e) => {
      console.log('Chat socket closed unexpectedly');
    };

    this.chatSocket.onmessage = (e) => {
      const data = JSON.parse(e.data);
      const message = `${data.user}: ${data.message}`;
      this.messages.push(message);
    };
  }

  newMessage = '';
  messages: string[] = [];

  chatSocket!: WebSocket;

  currentUserRole: string='';

  getCurrentUserRole() {
    this.authService.user().subscribe((user: any) => {
      this.currentUserRole = user.role;
    });
  }

  bookedAppointments:any[] = []; 

  pat_id:any=''

  chats:any[]=[];

  constructor(private authService:AuthService, private patientService:PatientService) {
    
    this.patientService.getChatHistory(this.tokeny).subscribe(
      (res:any)=>{
        this.chats=res;
        console.log("the patient chat towards doctor",res)
      }
      
    )
    this.getCurrentUserRole();
   
  }

  sendMessage(): void {
    if (this.newMessage.trim()) {
      this.chatSocket.send(this.newMessage);
      this.newMessage = '';
    }
  }

  removeMessage(message: string): void {
    const index = this.messages.indexOf(message);
    if (index !== -1) {
      this.messages.splice(index, 1);
    }
  }
}
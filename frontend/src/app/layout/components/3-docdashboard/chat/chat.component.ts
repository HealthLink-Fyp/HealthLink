import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs/operators';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { DoctorService } from 'src/app/architecture/services/doctor/doctor.service';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

import { environment } from 'src/environment/environment';

@Component({
  selector: 'app-chat1',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {

  constructor(private authService:AuthService,private doctorService:DoctorService, private patientService:PatientService) {
    
   
   
  }

  newMessage = '';
  messages: string[] = [];
 chatSocket!: WebSocket;
 bookedAppointments:any[] = []; 
 pat_id:any=''
  chats:any[]=[];

  ngOnInit(): void {
    this.onbookedAppointments();
    console.log("here are book appointments in chat doctor : ",this.bookedAppointments)
    
  }

  onbookedAppointments() {
    this.doctorService.getbookedAppointments().subscribe((appointments: any) => {
      const uniquePatients = Array.from(appointments.reduce((map:any, a:any) => {
        map.set(a.patient, { id: a.patient, name: a.patient_name });
        return map;
      }, new Map()).values());
      console.log('Unique patients:', uniquePatients); 
      this.bookedAppointments = uniquePatients;
    });
  }


 
  savePatId(patId: any) {
    console.log('Book Appointment clicked for ID:', patId);
    this.pat_id=patId;
    this.getChatHistory();
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
      const message = data.message
      this.messages.push(message);
    };
  }

  disconnect() {
    if (this.chatSocket) {
      this.chatSocket.close();
    }
  }

  ngOnDestroy() {
    this.disconnect();
    console.log("websocket connectiion closed")
  }

 

  getChatHistory()
  { 
    const patientData = {
      patient: this.pat_id
    };
   
    this.patientService.getChatHistory(patientData).subscribe(
      (res:any)=>{
        this.chats=res;
        console.log("the patient chat towards doctor",res)
      }
      
    )
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
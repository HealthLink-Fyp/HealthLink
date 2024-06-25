import { ElementRef, ViewChild, Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { DoctorService } from 'src/app/architecture/services/doctor/doctor.service';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';
import { environment } from 'src/environment/environment';
import { NgZone } from '@angular/core';

@Component({
  selector: 'app-chat1',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
})
export class ChatComponent implements OnInit {
  constructor(
    private authService: AuthService,
    private patientService: PatientService,
    private doctorService: DoctorService,
    private zone: NgZone
  ) {}

  @ViewChild('chatContainer') private chatContainer!: ElementRef;

  newMessage = '';
  messages: string[] = [];
  chatSocket!: WebSocket;
  bookedAppointments: any[] = [];
  dr_id: any = '';
  chats: any[] = [];
  profilePicture: string = '';
  selectedAppointmentId: number | null = null;

  ngOnInit(): void {
    this.onbookedAppointments();
  }

  onbookedAppointments() {
    this.patientService
      .getbookedAppointments()
      .subscribe((appointments: any) => {
        const uniqueDoctors = Array.from(
          appointments
            .reduce((map: any, a: any) => {
              map.set(a.doctor, { id: a.doctor, name: a.doctor_name });
              return map;
            }, new Map())
            .values()
        );
        console.log('Unique Doctors:', uniqueDoctors);
        this.bookedAppointments = uniqueDoctors;
      });
  }

  saveDocId(docId: any) {
    if (this.chatSocket && this.chatSocket.readyState === WebSocket.OPEN) {
      this.chatSocket.close(); // Close existing connection
    }
    this.selectedAppointmentId = docId;
    this.dr_id = docId;
    this.getChatHistory();
    this.createWebSocketConnection();
  }

  tokeny: any = '';

  createWebSocketConnection() {
    if (this.chatSocket && this.chatSocket.readyState === WebSocket.OPEN) {
      return; // Prevent creating a new connection if one is already open
    }
    const token = localStorage.getItem('token');
    this.tokeny = token;
    this.chatSocket = new WebSocket(
      `${environment.testApi}/${this.dr_id}/?token= ${token}`
    );

    this.chatSocket.onopen = (e) => {
      console.log('Chat socket successfully connected.');
    };

    this.chatSocket.onclose = (e) => {
      console.log('Chat socket closed unexpectedly');
    };

    this.chatSocket.onmessage = (e) => {
      const data = JSON.parse(e.data);
      const message = data.message;

      if (message.includes('joined')) {
        this.messages = [];
      }

      this.messages.push(message);
      this.scrollToBottom();
    };
  }

  scrollToBottom(): void {
    this.zone.runOutsideAngular(() => {
      setTimeout(() => {
        try {
          this.chatContainer.nativeElement.scrollTop =
            this.chatContainer.nativeElement.scrollHeight;
        } catch (err) {}
      });
    });
  }

  sendEmoji(): void {
    this.sendMessage('👍');
  }

  disconnect() {
    if (this.chatSocket) {
      this.chatSocket.close();
    }
  }

  ngOnDestroy() {
    this.disconnect();
    console.log('websocket connectiion closed');
  }

  getChatHistory() {
    const doctorData = {
      doctor: this.dr_id,
    };

    this.patientService.getChatHistory(doctorData).subscribe((res: any) => {
      this.chats = res;
    });
  }

  sendMessage(message: string | null = null): void {
    if (message) {
      this.newMessage = message;
    }

    if (this.newMessage.trim()) {
      this.chatSocket.send(this.newMessage);
      this.newMessage = '';
    }
    this.scrollToBottom();
  }

  removeMessage(message: string): void {
    const index = this.messages.indexOf(message);
    if (index !== -1) {
      this.messages.splice(index, 1);
    }
  }
}

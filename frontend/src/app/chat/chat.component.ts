import { Component } from '@angular/core';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent {
  newMessage = '';
  messages: string[] = [];

  chatSocket: WebSocket;

  constructor() {
    this.chatSocket = new WebSocket(`wss://organic-doodle-7v95g6qq45vwhr5wx-8000.app.github.dev/ws/chat/public_room/`);

    

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

  sendMessage(): void {
    if (this.newMessage.trim()) {
      this.chatSocket.send(JSON.stringify({ 'message': this.newMessage.trim() }));
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

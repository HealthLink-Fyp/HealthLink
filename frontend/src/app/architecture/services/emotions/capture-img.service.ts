import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { EmotifyService } from './emotify.service';

@Injectable({
  providedIn: 'root'
})
export class CaptureImgService {

  private canvas!: HTMLCanvasElement;
  private context!: CanvasRenderingContext2D;
  private video!: HTMLVideoElement;
  private stream: MediaStream | null = null; // Track the stream for later closing

  constructor(private http: HttpClient, private emotifyService: EmotifyService) { }

  async startImageCapture() {
    try {
      this.stream = await navigator.mediaDevices.getUserMedia({ video: true });
      this.video = document.createElement('video');
      this.video.srcObject = this.stream;

      // Wait for the video to be loaded to get its dimensions
      await new Promise((resolve) => {
        this.video.onloadedmetadata = () => {
          this.video.play();
          this.canvas = document.createElement('canvas');
          this.context = this.canvas.getContext('2d')!;
          this.canvas.width = this.video.videoWidth;
          this.canvas.height = this.video.videoHeight;
          resolve(true);
        };
      });

      // Start capturing images and pausing for 20 seconds
      await this.captureImageAndPauseLoop();
    } catch (error) {
      console.error('Error accessing camera:', error);
    }
  }

  async restartImageCapture() {
    // Stop capturing images and release the camera stream
    if (this.stream) {
      this.stream.getTracks().forEach(track => track.stop());
      this.stream = null;
    }

    // Pause for 5 seconds before restarting capture
    await new Promise(resolve => setTimeout(resolve, 10000)); 

    // Restart image capture
    if (!this.stream) {
      await this.startImageCapture();
    }
  }

  async captureImageAndPauseLoop() {
    while (true) {
      const imageData = await this.captureImage();
      console.log("usbrous",imageData);

      const imageBlob = new Blob([imageData], { type: 'image/jpeg' })

      // Send the image to the backend using EmotifyService
      const formData = new FormData();
      formData.append('file', imageBlob,'image.jpg');

      console.log("formdata file", formData.get('file'))

      await this.emotifyService.sendImage(formData);

      // Display the image on the screen
      const image = new Image();
      image.src = URL.createObjectURL(imageData);
      // document.body.appendChild(image);
      await this.restartImageCapture();

    }

    
  }

  async captureImage(): Promise<Blob> {
    this.context.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height);
    return new Promise((resolve) => {
      this.canvas.toBlob((blob) => {
        resolve(blob ?? new Blob());
      }, 'image/jpeg', 1);
    });
  }
}

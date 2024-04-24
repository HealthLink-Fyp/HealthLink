import { Component } from '@angular/core';

@Component({
  selector: 'app-swipe',
  templateUrl: './swipe.component.html',
  styleUrls: ['./swipe.component.css']
})
export class SwipeComponent {
  images: string[] = ['https://img1.wsimg.com/isteam/ip/e6e20e86-5501-4435-a039-a4d3c535c442/yelpariana.png/:/rs=w:1160','https://img1.wsimg.com/isteam/ip/e6e20e86-5501-4435-a039-a4d3c535c442/ylepvanessa.png/:/rs=w:1160','https://img1.wsimg.com/isteam/ip/e6e20e86-5501-4435-a039-a4d3c535c442/yelpsandra.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:1160,h:899']; // Array of image URLs
  slideIndex: number = 0;

  constructor() { }

  ngOnInit(): void {
    setInterval(() => {
      this.slideIndex = (this.slideIndex + 1) % this.images.length;
    }, 5000); // Change slide every 5 seconds
  }
}

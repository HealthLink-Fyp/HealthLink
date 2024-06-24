import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environment/environment';

@Component({
  selector: 'app-lay1',
  templateUrl: './lay1.component.html',
  styleUrls: ['./lay1.component.css'],
})
export class Lay1Component {
  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.bootBackend();
  }

  bootBackend() {
    const url = environment.api.replace('api/v1', '');
    this.http.get(url).subscribe({
      next: () => {
        console.log('Backend is up');
      },
      error: (err) => {
        console.error('Error connecting to backend:', err);
      },
    });
  }
}

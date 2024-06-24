import { AuthService } from 'src/app/architecture/services/auth.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environment/environment';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css'],
})
export class AuthComponent implements OnInit {
  message = '';
  amWho = '';

  constructor(
    private authService: AuthService,
    private router: Router,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    this.authService.user().subscribe({
      next: (res: any) => {
        this.message = `Hi ${res.first_name} ${res.last_name}`;

        this.amWho = res.role;
        console.log('role', this.amWho);
        this.profileExist(this.amWho);
        AuthService.authEmitter.emit(true);
      },
      error: (err) => {
        this.message = 'You are not logged in';
        AuthService.authEmitter.emit(false);
      },
    });
  }

  profileExist(role: string) {
    this.http
      .get(`${environment.api}/auth/profile/`, { observe: 'response' })
      .subscribe({
        next: (res: any) => {
          if (res.body && res.status === 200 && role) {
            this.router.navigate([`/${role}/dashboard`]);
          } else {
            this.router.navigate([`/${role}/form`]);
          }
        },
        error: (err) => {
          console.log('error', err);
        },
      });
  }
}

import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/architecture/services/auth.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  form!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router,
  ) {}

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      email: '',

      password: '',
    });
  }

  submit() {
    this.authService.login(this.form.getRawValue()).subscribe((res: any) => {
      this.authService.accessToken = res.access_token;
      AuthService.authEmitter.emit(true);
      this.router.navigate(['/auth']);


      const token = res.access_token;
      // Store the token in local storage
    localStorage.setItem('token', token);
    });
  }
}

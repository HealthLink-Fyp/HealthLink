import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { NotifyService } from '../../notification/notify.service';


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
    private notifyService:NotifyService
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

      if(res.access_token)
        {
          this.notifyService.showSuccess("logged in successfully!");
        }
    
      AuthService.authEmitter.emit(true);

  
   
    

      this.router.navigate(['/auth']);
      

      const token = res.access_token;
      // Store the token in local storage
    localStorage.setItem('token', token);
    },
    error => {
      console.error('Error:', error)
      this.notifyService.showError(' Wrong Credentials ! Try again')
    }
  );
  }
}

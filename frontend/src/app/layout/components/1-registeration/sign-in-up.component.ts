
import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormControl,
  FormGroup,
  Validators,
} from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { NotifyService } from '../notification/notify.service';

@Component({
  selector: 'app-sign-in-up',
  templateUrl: './sign-in-up.component.html',
  styleUrls: ['./sign-in-up.component.css']
})
export class SignInUpComponent {
  form!: FormGroup;
  isUpdateMode = false;  

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router,
    private route:ActivatedRoute,
    private notifyService:NotifyService
  ) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe(params=>{
      this.isUpdateMode=params['updateMode'] ||false;        //catch the boolean value from dashboard compoent
      this.createForm();                                     //create the entire form fields
      if (this.isUpdateMode) {                               //if update is true
        this.getUserDataFields();                         // fill out the form fields with user data
      }
    })
  }

  createForm()
  {
    this.form = this.formBuilder.group({
      first_name: '',

      last_name: '',

      username: '',

      email: '',

      password: '',

      phone_number: '',

      address: '',

      city: '',

      role: '',
    });
  }

  submit() {
    const method = this.isUpdateMode ? 'updateUser' : 'register';  
    this.authService[method](this.form.getRawValue())
      .subscribe(() => this.router.navigate(['/account/login']));
      this.notifyService.showSuccess('Well Done, the account has been created !');
  }

  getUserDataFields() {
    this.authService.user().subscribe(data => this.form.patchValue(data));   //re-write the user data on the form fields
  }

  
  toggleUpdateMode() {                               //used for cancel button which empties out the form fields and does not update the form
    this.isUpdateMode = !this.isUpdateMode;
    
  }


}

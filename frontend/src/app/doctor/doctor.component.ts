import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormArray, FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { DoctorService } from '../services/doctor/doctor.service';
import {SPECIALIZATION_CHOICES,QUALIFICATION_CHOICES,availableDays} from './doctorExtras'

@Component({
  selector: 'app-doctor',
  templateUrl: './doctor.component.html',
  styleUrls: ['./doctor.component.css'],
})
export class DoctorComponent implements OnInit {
  form!: FormGroup;
  message = '';
  authenticated = false;

  SPECIALIZATION_CHOICES=SPECIALIZATION_CHOICES;
  QUALIFICATION_CHOICES=QUALIFICATION_CHOICES;
  availableDays=availableDays;
  

  constructor(
    private formBuilder: FormBuilder,
    private doctorService: DoctorService,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    AuthService.authEmitter.subscribe((authenticated) => {
      this.authenticated = authenticated;
    });

    this.form = this.formBuilder.group({
      specialization: '',
      qualification: '',
      experience_years: '',
      city: '',

      available_timings: '',

      consultation_fees: '',

      availability_data:this.formBuilder.group({
        days: this.formBuilder.array([]),// Initialize as an empty array
        start:'',
        end:''
      }),

      summary: '',
      wait_time: '',
    });
  }

  onChange(e:any)
  {
    const checkedvalue=e.target.value;
    const checkedflag=e.target.checked;

    const checkedArray=this.form.get('availability_data.days') as FormArray;
    if(checkedflag)
    {
      checkedArray.push(new FormControl(checkedvalue))
    }
    else
    {
      let i:number=0;
      checkedArray.controls.forEach((item)=>{
        if(item.value==checkedflag)
        {
          checkedArray.removeAt(i);
        }
        i++;
      })
    }

   
  }

  submit() {
    this.doctorService
      .register(this.form.getRawValue())
      .subscribe((res) => console.log(res));
    this.router.navigate(['/dboard']);
  }

  Done() {
    this.router.navigate(['/dboard']);
  }
}

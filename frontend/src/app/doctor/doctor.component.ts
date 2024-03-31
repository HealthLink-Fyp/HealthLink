import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormArray, FormControl } from '@angular/forms';
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
  
  message = '';

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
    let doctor_data = this.prepareDoctorData();
    this.doctorService
      .register(doctor_data)
      .subscribe((res) => console.log(res));
    this.router.navigate(['/dboard']);
  }

  prepareDoctorData() {
    let formValue = this.form.getRawValue();

    let availability_data = {
      days: formValue.available_days,
      start: formValue.start_time,
      end: formValue.end_time,
    };

    let doctor_data = {
      specialization: formValue.specialization,
      qualification: formValue.qualification,
      experience_years: formValue.experience_years,
      city: formValue.city,
      consultation_fees: formValue.consultation_fees,
      summary: formValue.summary,
      wait_time: formValue.wait_time,
      availability_data: availability_data,
    };

    return doctor_data;
  }

  Done() {
    this.router.navigate(['/dboard']);
  }
}

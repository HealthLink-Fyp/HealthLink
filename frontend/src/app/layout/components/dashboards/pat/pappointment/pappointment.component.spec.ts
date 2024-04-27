import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PappointmentComponent } from './pappointment.component';

describe('PappointmentComponent', () => {
  let component: PappointmentComponent;
  let fixture: ComponentFixture<PappointmentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PappointmentComponent]
    });
    fixture = TestBed.createComponent(PappointmentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

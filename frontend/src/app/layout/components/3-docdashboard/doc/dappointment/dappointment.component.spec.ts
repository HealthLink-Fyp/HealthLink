import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DappointmentComponent } from './dappointment.component';

describe('DappointmentComponent', () => {
  let component: DappointmentComponent;
  let fixture: ComponentFixture<DappointmentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DappointmentComponent]
    });
    fixture = TestBed.createComponent(DappointmentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

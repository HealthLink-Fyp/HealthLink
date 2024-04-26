import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MedrecordComponent } from './medrecord.component';

describe('MedrecordComponent', () => {
  let component: MedrecordComponent;
  let fixture: ComponentFixture<MedrecordComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MedrecordComponent]
    });
    fixture = TestBed.createComponent(MedrecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

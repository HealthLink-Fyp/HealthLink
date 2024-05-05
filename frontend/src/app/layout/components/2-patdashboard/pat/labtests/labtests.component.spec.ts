import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LabtestsComponent } from './labtests.component';

describe('LabtestsComponent', () => {
  let component: LabtestsComponent;
  let fixture: ComponentFixture<LabtestsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LabtestsComponent]
    });
    fixture = TestBed.createComponent(LabtestsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

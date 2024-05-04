import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PatComponent } from './pat.component';

describe('PatComponent', () => {
  let component: PatComponent;
  let fixture: ComponentFixture<PatComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PatComponent]
    });
    fixture = TestBed.createComponent(PatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

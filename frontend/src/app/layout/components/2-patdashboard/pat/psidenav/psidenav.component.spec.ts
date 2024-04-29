import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PsidenavComponent } from './psidenav.component';

describe('PsidenavComponent', () => {
  let component: PsidenavComponent;
  let fixture: ComponentFixture<PsidenavComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PsidenavComponent]
    });
    fixture = TestBed.createComponent(PsidenavComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

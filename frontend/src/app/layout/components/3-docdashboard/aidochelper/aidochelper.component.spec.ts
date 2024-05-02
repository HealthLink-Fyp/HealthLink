import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AidochelperComponent } from './aidochelper.component';

describe('AidochelperComponent', () => {
  let component: AidochelperComponent;
  let fixture: ComponentFixture<AidochelperComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AidochelperComponent]
    });
    fixture = TestBed.createComponent(AidochelperComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

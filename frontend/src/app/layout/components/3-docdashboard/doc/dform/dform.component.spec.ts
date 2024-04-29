import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DformComponent } from './dform.component';

describe('DformComponent', () => {
  let component: DformComponent;
  let fixture: ComponentFixture<DformComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DformComponent]
    });
    fixture = TestBed.createComponent(DformComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

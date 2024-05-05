import { TestBed } from '@angular/core/testing';

import { CaptureImgService } from './capture-img.service';

describe('CaptureImgService', () => {
  let service: CaptureImgService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CaptureImgService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

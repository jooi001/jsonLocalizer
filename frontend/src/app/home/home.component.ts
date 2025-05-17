import { Component, OnInit } from '@angular/core';
import { NgClass, NgIf, CommonModule } from '@angular/common';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [NgClass, NgIf], // or just CommonModule to get both
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  file: any;
  getFile(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (!input.files || input.files.length === 0) {
      console.error('No file selected');
      return;
    }

    this.file = input.files[0];
    console.log("File selected:", this.file);
  }

  uploadFile() {
    let formData = new FormData();
    formData.set('file', this.file);

    if (!this.file) {
      console.error('No file selected for upload');
      return;
    }

    this.apiService.post(formData).subscribe(
      (response: any) => {
        console.log("File uploaded successfully:", response);
      },
      (error: any) => {
        console.error("Error uploading file:", error);
      }
    );
  }

  clearFile(): void {
    this.file = null;
  }

  ngOnInit(): void {
    // Initialization logic can go here
  }
}
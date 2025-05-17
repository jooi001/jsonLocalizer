import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  message: string = '';

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getMessage().subscribe(
      (data) => {
        this.message = data.message;
      },
      (error) => {
        console.error('Error fetching message:', error);
      }
    );
  }
}
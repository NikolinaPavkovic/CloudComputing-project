package com.example.unsapp.service;

import com.example.unsapp.dto.StudentDTO;
import com.example.unsapp.model.Student;

public interface StudentService {
    Student saveStudent(StudentDTO dto);
}

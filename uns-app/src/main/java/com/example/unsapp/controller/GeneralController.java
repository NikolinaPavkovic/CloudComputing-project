package com.example.unsapp.controller;

import com.example.unsapp.dto.ProfessorDTO;
import com.example.unsapp.dto.StudentDTO;
import com.example.unsapp.model.Professor;
import com.example.unsapp.model.Student;
import com.example.unsapp.service.ProfessorService;
import com.example.unsapp.service.StudentService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("/uns-app")
public class GeneralController {
    private final StudentService studentService;
    private final ProfessorService professorService;

    @PostMapping("/student")
    public ResponseEntity<String> saveStudent(@RequestBody StudentDTO studentDTO){
        Student student = studentService.saveStudent(studentDTO);
        if (student == null)
            return new ResponseEntity<>("Student already exists.", HttpStatus.OK);
        return new ResponseEntity<>("OK", HttpStatus.OK);
    }

    @PostMapping("/professor")
    public ResponseEntity<String> saveProfessor(@RequestBody ProfessorDTO professorDTO){
        Professor professor = professorService.saveProfessor(professorDTO);
        if (professor == null)
            return new ResponseEntity<>("Professor already exists.", HttpStatus.OK);
        return new ResponseEntity<>("OK", HttpStatus.OK);
    }
}

package com.example.unsapp.service;

import com.example.unsapp.dto.StudentDTO;
import com.example.unsapp.model.Student;
import com.example.unsapp.repository.StudentRepository;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.modelmapper.ModelMapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
@Transactional
public class StudentServiceImpl implements  StudentService{
    private final StudentRepository studentRepository;
    private final ModelMapper mapper = new ModelMapper();
    @Override
    public Student saveStudent(StudentDTO dto) {
        List<Student> allStudents = studentRepository.findAll();
        for (Student student: allStudents) {
            if (student.getEmail().equals(dto.getEmail()) || student.getIndex().equals(dto.getIndex())) {
                return null;
            }
        }
        Student student = mapper.map(dto, Student.class);
        System.out.println(student);
        return studentRepository.save(student);
    }
}

package com.example.unsapp.service;

import com.example.unsapp.dto.ProfessorDTO;
import com.example.unsapp.model.Professor;
import com.example.unsapp.model.Student;
import com.example.unsapp.repository.ProfessorRepository;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.modelmapper.ModelMapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
@Transactional
public class ProfessorServiceImpl implements ProfessorService{
    private final ProfessorRepository professorRepository;
    private final ModelMapper mapper = new ModelMapper();
    @Override
    public Professor saveProfessor(ProfessorDTO dto) {
        List<Professor> allprofessors = professorRepository.findAll();
        for (Professor professor: allprofessors) {
            if (professor.getEmail().equals(dto.getEmail())) {
                return null;
            }
        }
        Professor professor = mapper.map(dto, Professor.class);
        System.out.println(professor);
        return professorRepository.save(professor);
    }
}

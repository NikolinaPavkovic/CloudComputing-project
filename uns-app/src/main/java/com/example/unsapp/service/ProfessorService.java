package com.example.unsapp.service;

import com.example.unsapp.dto.ProfessorDTO;
import com.example.unsapp.model.Professor;

public interface ProfessorService {
    Professor saveProfessor(ProfessorDTO dto);
}

package com.example.unsapp.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ProfessorDTO {
    private String firstname;
    private String lastname;
    private String email;
}

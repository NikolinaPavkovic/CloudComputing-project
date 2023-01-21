package com.example.unsapp.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "professors")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Professor {
    @Id
    @Column(name = "id", nullable = false)
    @SequenceGenerator(name = "professorSeqGen", sequenceName = "professorSeqGen", initialValue = 1, allocationSize = 1)
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "professorSeqGen")
    private Long id;

    @Column(name="firstname", nullable=false)
    private String firstname;

    @Column(name="lastname", nullable=false)
    private String lastname;

    @Column(name="email", nullable=false)
    private String email;
}

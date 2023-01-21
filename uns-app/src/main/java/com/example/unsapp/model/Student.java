package com.example.unsapp.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "students")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Student {
    @Id
    @Column(name = "id", nullable = false)
    @SequenceGenerator(name = "studentSeqGen", sequenceName = "studentSeqGen", initialValue = 1, allocationSize = 1)
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "studentSeqGen")
    private Long id;

    @Column(name="index", nullable=false)
    private String index;

    @Column(name="firstname", nullable=false)
    private String firstname;

    @Column(name="lastname", nullable=false)
    private String lastname;

    @Column(name="email", nullable=false)
    private String email;

}

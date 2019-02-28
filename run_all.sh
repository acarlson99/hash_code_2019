#! /bin/bash

echo 'Running a_example.txt'
./main.py input/a_example.txt
mv the_answer.txt a_answer.txt

echo 'Running b_lovely_landscapes.txt'
./main.py input/b_lovely_landscapes.txt
mv the_answer.txt b_answer.txt

echo 'Running c_memorable_moments.txt'
./main.py input/c_memorable_moments.txt
mv the_answer.txt c_answer.txt

echo 'Running d_pet_pictures.txt'
./main.py input/d_pet_pictures.txt
mv the_answer.txt d_answer.txt

echo 'Running e_shiny_selfies.txt'
./main.py input/e_shiny_selfies.txt
mv the_answer.txt e_answer.txt

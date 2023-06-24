#!/bin/bash
quit=0
again() { 
    echo "(1) try another"
    echo "(2) quit"
  read YorN
  case $YorN  in
     1) joke_menu ;;
     2) quit=1 ;;
     *) echo "invalid input" && again 
  esac
}

enter_answer() { echo "enter answer" ;}
correct() { echo "THATS CORRECT!" ;}

correct_ans_is="Not quite, the correct answer is: "

joke_menu() { 
    echo "select a joke"
    echo "(1) What do you call blackbirds that stick together?"
    echo "(2) What do you call a tiny mother?"
    echo "(3) What do you call something that goes up when the rain comes down?"
    echo "(4) What do you call someone that saw an iPhone being stolen?"
    echo "(5) What do you call a frozen kid?"
    echo "(6) quit"
  read jokenum 
  case $jokenum in
    1) enter_answer && read a1 && [ $a1 = "velcrows" ] && correct || echo "$correct_ans_is velcrows" && again ;;
    2) enter_answer && read a2 && [ $a2 = "minimum" ] && correct || echo "$correct_ans_is a minimum" && again ;;
    3) enter_answer && read a3 && [ $a3 = "umbrella" ] && correct || echo "$correct_ans_is an umbrella" && again ;;
    4) enter_answer && read a4 && [ $a4 = "iwitness" ] && correct || echo "$correct_ans_is iwitness" && again ;;
    5) enter_answer && read a5 && [ $a5 = "chilldren" ] && correct || echo "$correct_ans_is chilldren" && again ;;
    6) quit=1 ;; 
      *) echo "invalid input" && again ;;
  esac
  }

while [ $quit -eq 0 ] ; do
  joke_menu
done
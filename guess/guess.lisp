(defparameter *small* 1)
(defparameter *big* 100)

(defun guess-my-number ()
    (ash (+ *small* *big*) -1))

(defun smaller ()
    (setf *big* (1- (guess-my-number)))
    (guess-my-number))

(defun bigger ()
    (setf *small* (1+ (guess-my-number)))
    (guess-my-number))

(defun start-over ()
    (defparameter *small* 1)
    (defparameter *big* 100)
    (guess-my-number))

(defun correct ()
    (print "Bzzt! Yay, you and Computer win! Type (start-over) to play again.")
)

(print "############################")
(print "GUESS MY NUMBER")
(print "Directions:")
(print "Pick a number 1 through 100.")
(print "Type (guess-my-number) to start.")
(print "Enter (lower) if the computers guesses too high.")
(print "Enter (bigger) if the computers guesses too low.")
(print "############################")
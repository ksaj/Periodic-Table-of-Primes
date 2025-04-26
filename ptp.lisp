(defun prime-p (n)
	(and (> n 1)
		(loop for i from 2 to (isqrt n) never (zerop (mod n i)))))

(defun generate-primes (limit)
	(loop for n from 2 below limit when (prime-p n) collect n))

(defun create-prime-table (limit &optional (columns 6))
	(let* ((primes (generate-primes limit))
			(rows (+ 1 (truncate limit columns)))
			(table (make-array (list rows columns) :initial-element " .")))
		(dolist (p primes)
			(let ((row (truncate p columns))
					(col (mod p columns)))
				(setf (aref table row col)
						(format nil "~3D" p))))
		table))

(defun print-prime-table (table columns)
	(format t "Periodic Table of Primes (mod ~A):~%~%" columns)
	(format t "mod |")
	(loop for i below columns do (format t "~5A " i))
	(format t "~%----------------------------------------~%")
	(loop for row from 0 below (array-dimension table 0) do
		 (format t "~3D |" (* row columns))
		 (loop for col from 0 below columns do
				(format t "~5A " (aref table row col)))
		 (format t "~%")))

;; Usage example:
(let ((table (create-prime-table 100)))
	(print-prime-table table 6))


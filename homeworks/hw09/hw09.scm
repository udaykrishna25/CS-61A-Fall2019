
; Tail recursion

(define (replicate x n)
  (define (replicate-tail k i)
    (if (= k n)
        i
        (replicate-tail (+ k 1) (cons x i))))
  (replicate-tail 0 nil))

(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (accumulate combiner
                            start
                            (- n 1)
                            term)
                        (term n))
))

(define (accumulate-tail combiner start n term)
  (if (= n 0)
      start
      (accumulate-tail combiner (combiner (term n) start) (- n 1) term)
))
; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three (cons-stream 3
    (map-stream (lambda (x) (+ 3 x)) multiples-of-three)))

(define (nondecreastream s)
    (define (helper prev stream sofar)
        (if (null? stream)
            (cons-stream sofar nil)
            (if (<= prev (car stream))
                (helper (car stream) (cdr-stream stream) (append sofar (list (car stream))))
                (cons-stream sofar (nondecreastream stream)))))
            (helper (car s) s nil)
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))
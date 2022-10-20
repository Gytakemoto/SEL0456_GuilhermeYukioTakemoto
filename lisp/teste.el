(defun f (x)                                                     ;; Definindo a função f (quadrada) 
  (* x x))

(f 2)

(defun fact(x)                                                   ;; Definindo a função fact (fatorial)
  (if (= x 0)
      1
    (*x (facr (- x 1)))))

(fact 4)

(setq l '(1 2 3 4))                                              ;; Definindo a lista l e atribuindo l = [1 2 3 4]
(defun list-quad (l fcn)                                         ;; Definindo a função list-quad bem como a função que cada elemento irá passar (fcn)
  (and l                                                         ;; Se l estiver vazio, and l = 0
       (cons (funcall fcn (car l))                               ;; 
             (list-quad (cdr l) fcn))))

(list-quad '(1 2 3 4 5) #'fact)
(list-quad '("abc"  "de" "fghi") #'lenght)
(mapcar (lambda (x) (* x x x)) (list 1 2 3 5))

(defun cube (x)
  (* x x x ))

(mapcar #'cube (list 1 2 3 5))                                   ;; mapcar atribui à função definida cada elemento da lista de entrada
(setq f (lambda (x) (* x x x)))
(f 2)
(setq n '())
(mapcar (lambda (x) (* (car x) (cadr x))) '(( 1 2) (2 3) (4 5))) ;; car acessa o primeiro valor de uma lista (1,2): (1). cadr seria o segundo (2)

let()

(defun fx ()
  "Documento da função fx: ela retorna string 'último'."
  "sempre"
  "retorna"
  "o"
  "ultimo"

(setq w (fx))

(documentation #'fx)                                             ;; Retorna a primeira string de função
(documentation #'funcall)

(let ((x 5))
  (while (> x 0)
    (insert x)
    (setq x (- x 1))))^E^D^C^B^A

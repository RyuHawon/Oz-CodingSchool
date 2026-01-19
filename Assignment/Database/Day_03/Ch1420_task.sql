-- employees 테이블을 생성해주세요
--     - 속성명 **id의** 자료형은 INT입니다. 추가로 자동으로 1씩 증가하도록 설정하고 기본키로 지정합니다.
--     - 속성명 **name의** 자료형은 VARCHAR(100)입니다.
--     - 속성명 **position의** 자료형은 VARCHAR(100)입니다.
--     - 속성명 **salary의** 자료형은 DECIMAL(10, 2)입니다.
CREATE DATABASE assignment;
USE assignment;
CREATE TABLE employees(
	id INT AUTO_INCREMENT PRIMARY KEY,
 	username VARCHAR(100),
 	`position` VARCHAR(100),
 	salary DECIMAL(10, 2)
);

-- 직원 데이터를 `employees`에 추가해주세요
--     - 이름: 혜린, 직책: PM, 연봉: 90000
--     - 이름: 은우, 직책: Frontend, 연봉: 80000
--     - 이름: 가을, 직책: Backend, 연봉: 92000
--     - 이름: 지수, 직책: Frontend, 연봉: 7800
--     - 이름: 민혁, 직책: Frontend, 연봉: 96000
--     - 이름: 하온, 직책: Backend, 연봉: 130000
INSERT INTO assignment.employees(id, name, `position`, salary)
VALUES
	(1, '혜린', 'PM', 90000),
    (2, '은우', 'Frontend', 80000),
    (3, '가을', 'Backend', 92000),
    (4, '지수', 'Frontend', 7800),
    (5, '민혁', 'Frontend', 96000),
    (6, '하온', 'Backend', 130000);

-- 모든 직원의 이름과 연봉 정보만을 조회하는 쿼리를 작성해주세요
SELECT name, salary
FROM assignment.employees;

-- Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요.
SELECT name, salary
FROM assignment.employees
WHERE `position` = 'Frontend' AND salary <= 90000;

-- PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요.
SET SQL_SAFE_UPDATES = 0;
UPDATE assignment.employees
SET salary = salary * 1.1
WHERE `position` = 'PM';

SELECT * FROM assignment.employees WHERE `position` = 'PM';

-- 모든 Backend' 직책을 가진 직원의 연봉을 5% 인상하세요.
UPDATE assignment.employees
SET salary = salary * 1.05
WHERE `position` = 'Backend';

SELECT * FROM assignment.employees WHERE `position` = 'Backend';

-- 민혁 사원의 데이터를 삭제하세요
DELETE FROM assignment.employees WHERE name = '민혁';

-- 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.
SELECT `position`, AVG(salary) FROM assignment.employees GROUP BY `position`;

-- employees 테이블을 삭제하세요.
DROP TABLE employees;




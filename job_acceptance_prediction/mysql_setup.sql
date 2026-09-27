CREATE DATABASE IF NOT EXISTS job_acceptance_db;
USE job_acceptance_db;
CREATE TABLE IF NOT EXISTS job_acceptance (candidate_id INT PRIMARY KEY, age INT, education VARCHAR(100), experience INT, current_salary DECIMAL(12,2), offered_salary DECIMAL(12,2), job_role VARCHAR(100), location VARCHAR(100), work_mode VARCHAR(50), relocation VARCHAR(20), career_growth VARCHAR(50), acceptance VARCHAR(20));
SELECT COUNT(*) AS total_candidates FROM job_acceptance;
SELECT acceptance,COUNT(*) AS candidate_count FROM job_acceptance GROUP BY acceptance;

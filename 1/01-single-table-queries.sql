-- 01. Querying data
SELECT 
  LastName
FROM
  employees;

-- 01-2. 성과 이름 함께 조회하기 (select는 한개이상 작성 가능)
SELECT
  LastName, FirstName
FROM
  employees;

  -- 01-3. 모든 정보 조회하기기
SELECT
  *
FROM
  employees;


-- 01-4. 필드명 바꿔서 조회하기 -> 실제 db는 변경되지 않음 
SELECT
  FirstName AS '이름'
FROM
  employees;

-- 01-5. 60000으로 나눠 분 단위 값으로 출력 
SELECT
  NAME,
  Milliseconds / 60000 AS '재생시간(분)'
FROM
tracks;

-- 02. Sorting data (오름차순 정렬)
SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName;

-- 02-1. 내림차순 정렬 
SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

-- NULL 정렬 예시 (NULL이 존재할시, NULL 먼저 출력)
SELECT 
  postalCode
FROM
  customers
ORDER BY
  postalCode;

-- 02-2 (Country 우선 내림차순 정렬, 그 안에서 City 정렬)
SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC, 
  City;

-- 02-3. 재생시간이 가장 긴 
SELECT
  Name,
  Milliseconds / 60000 AS '재생시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- 03. Filtering data (distinct: 중복 제거)
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

-- 03-1. where: 특정 검색 조건 지정 
SELECT 
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

-- 03-2. != 비교 연산자 연습 
SELECT 
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

-- 03-3. AND 연산자
SELECT 
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country == 'USA';

-- 03-4. OR 연산자
SELECT 
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country == 'USA';

-- 03-5. BETWEEN 연산자 (부등호도 가능)
SELECT 
  Name, Bytes
FROM
  tracks
-- WHERE
--   Bytes BETWEEN 100000 AND 500000;
WHERE
  Bytes >= 100000
  AND Bytes <= 500000;

-- 03-6. BETWEEN과 ORDER BY 함께 사용 (where, order by 순으로 작성해야만 함 !)
SELECT 
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
   Bytes;


-- 03-7. IN 연산자 
-- IN, ==는 딱 정확히 저 글자만 있는 데이터 조회할 때 
SELECT 
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France');
-- WHERE
--   Country = 'Canada'
--   OR Country = 'Germany'
--   OR Country = 'France';

-- 03-7. NOT IN 연산자 
SELECT 
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France');

-- 03-8. LastName이 son으로 끝나는 데이터의 성과 이름 조회 
-- LIKE 는 IN, ==과 다르게 특정 글자가 포함되기만 하면 됨
SELECT 
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

-- 03-9. FirstName이 4자리면서 a로 끝나는 데이터 LastName, FirstName 조회 
SELECT 
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';

-- 05-1. TrackId, Name, Bytes 데이터를 Bytes 기준 내림차순으로 7개 데이터만 조회 
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT
  7;

-- 05-2. TrackId, Name, Bytes 데이터를 Bytes 기준 내림차순으로 4~7번째 데이터만 조회 
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT
  3,4;
-- LIMIT
--   4
-- OFFSET
--   3;

-- 04-1. Grouping data (GROUP BY는 중복제거 및 정렬 기능, 국가별 고객 수 구하기)
SELECT 
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

-- 04-2. Bytes의 평균 값을 내림차순 조회 
SELECT 
  Composer,
  AVG(Bytes) AS avgOfBytes
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  avgOfBytes DESC;

-- 04-3.Milliseconds의 평균 값이 10미만인 데이터 조회 (주석 코드는 에러 발생)
-- HAVING은 주로, GROUP BY와 함께 사용되며 GROUP BY가 없다면 WHERE처럼 동작 
SELECT 
  Composer,
  AVG(Milliseconds / 60000) AS avgOfBytes
FROM
  tracks
-- GROUP BY
--   avgOfBytes < 10
-- ORDER BY
--   Composer;
GROUP BY
  Composer
HAVING
  avgOfBytes < 10;
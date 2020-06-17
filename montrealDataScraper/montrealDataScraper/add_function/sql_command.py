
class sql_cmd:
    def __init__(self, boroughname):
        self._boroughname = boroughname

    def testing_command(self):
        command = '''
        
        
        '''
        return command

    def borough_inf(self):
        command = '''
WITH Y AS
(with X as (SELECT
        id,
        boroughname,
        confirmedCase,
        Date,
        time
FROM
DATA
WHERE boroughname = "'''+self._boroughname+'''")

SELECT *,
(SELECT Date FROM X X1
       WHERE X1.Date > X.Date
          OR X1.Date = X.Date AND X1.id > X.id
       ORDER BY Date , ID  LIMIT 1 ) next 
FROM
X
ORDER BY date, id)
select id, boroughname,confirmedcase,date,time
FROM
Y
WHERE
date <> next
AND
next <> 0
        '''
        return command

    def borough_inf_0error(self):
        command ='''
            with boroughList AS(
        WITH Y AS
        (with X as (SELECT
                id,
                boroughname,
                confirmedCase,
                Date,
                time
        FROM
        DATA
        WHERE boroughname = "''' + self._boroughname + '''")

        SELECT *,
        (SELECT Date FROM X X1
               WHERE X1.Date > X.Date
                  OR X1.Date = X.Date AND X1.id > X.id
               ORDER BY Date , ID  LIMIT 1 ) next 
        FROM
        X
        ORDER BY date, id)
        select id, boroughname,confirmedcase,date,time
        FROM
        Y
        WHERE
        date <> next
        AND
        next <> 0)

        select *
        from 
        boroughList
        where 
        confirmedCase <> -1
        and 
        date >ifnull((
        select date
        from 
        boroughList
        where 
        confirmedCase = -1
        ),0)
                    '''
        return command


    def borough_case(self):
        command ='''
    WITH
    Y
    AS
    (with X as (SELECT
     id,
     boroughname,
     confirmedCase,
     Date,
     time
     FROM
     DATA
     WHERE boroughname = "''' + self._boroughname + '''")

    SELECT *,
    (SELECT Date FROM X X1
    WHERE X1.Date > X.Date
    OR X1.Date = X.Date AND X1.id > X.id
    ORDER BY Date, ID  LIMIT 1)
    next
    FROM
    X
    ORDER
    BY
    date, id)
    select
    confirmedcase , date
    FROM
    Y
    WHERE
    date <> next
    AND
    next <> 0
        '''
        return command

    def borough_inf_0error_case_only(self):
        command ='''
            with boroughList AS(
        WITH Y AS
        (with X as (SELECT
                id,
                boroughname,
                confirmedCase,
                Date,
                time
        FROM
        DATA
        WHERE boroughname = "''' + self._boroughname + '''")

        SELECT *,
        (SELECT Date FROM X X1
               WHERE X1.Date > X.Date
                  OR X1.Date = X.Date AND X1.id > X.id
               ORDER BY Date , ID  LIMIT 1 ) next 
        FROM
        X
        ORDER BY date, id)
        select id, boroughname,confirmedcase,date,time
        FROM
        Y
        WHERE
        date <> next
        AND
        next <> 0)

        select confirmedcase , DATE
        from 
        boroughList
        where 
        confirmedCase <> -1
        and 
        date >ifnull((
        select date
        from 
        boroughList
        where 
        confirmedCase = -1
        ),0)
                    '''
        return command

    def borough_daily_increase(self):
        command = '''
with tableCorrect as(
 with boroughList AS(
        WITH Y AS
        (with X as (SELECT
                id,
                boroughname,
                confirmedCase,
                Date,
                time
        FROM
        DATA
        WHERE boroughname = "''' + self._boroughname + '''")

        SELECT *,
        (SELECT Date FROM X X1
               WHERE X1.Date > X.Date
                  OR X1.Date = X.Date AND X1.id > X.id
               ORDER BY Date , ID  LIMIT 1 ) next 
        FROM
        X
        ORDER BY date, id)
        select id, boroughname,confirmedcase,date,time
        FROM
        Y
        WHERE
        date <> next
        AND
        next <> 0)

        select confirmedcase,date as date_formal, DATETIME(date)as date, DATETIME(date, '+1 day') as nextDay
        from 
        boroughList
        where 
        confirmedCase <> -1
        and 
        date >ifnull((
        select date
        from 
        boroughList
        where 
        confirmedCase = -1
        ),0)
   )
   
SELECT 
      CASE (t1.confirmedCase<t2.confirmedcase) 
           WHEN 1
               THEN 0
           ELSE (t1.confirmedCase-t2.confirmedcase) 
       END Increase,
t1.date_formal as date
FROM tableCorrect as t1
CROSS JOIN tableCorrect as t2
where t1.DATE = t2.nextDay
 
        '''
        return command

    def update_cumulative_N_date(self, cumulative, date):
        command = '''
        UPDATE
        REPORT
        set
        cumulativecases = '''+str(cumulative)+''', cumulativeCasesDate = "'''+str(date)+'''"
        WHERE
        boroughname = "''' + self._boroughname + '''";
         '''
        return command

    def update_new_case_N_date(self, new_case, date):
        command = '''
        UPDATE
        REPORT
        set
        newCases = '''+str(new_case)+''', newCasesDate = "'''+str(date)+'''"
        WHERE
        boroughname = "''' + self._boroughname + '''";
         '''
        return command

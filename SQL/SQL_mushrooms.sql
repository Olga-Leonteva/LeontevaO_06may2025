SELECT distinct name
FROM Regions;

SELECT m.name, m.season, m.edible
FROM Mushrooms AS m
LEFT JOIN Categories AS c
ON m.category_id=c.category_id
WHERE c.name='Трубчатые';

SELECT c.name, COUNT(*)
FROM Categories AS c
LEFT JOIN Mushrooms AS m
ON m.category_id=c.category_id
GROUP BY c.name
ORDER BY COUNT (*) DESC;

SELECT m.name, m.description
FROM Mushrooms AS m
LEFT JOIN Regions AS r
ON m.primary_region_id=r.region_id
WHERE m.edible='true'
ORDER BY r.size DESC
LIMIT 5;

SELECT m.name
FROM Mushrooms AS m
LEFT JOIN Categories AS c
ON m.category_id=c.category_id
LEFT JOIN Regions AS r
ON m.primary_region_id=r.region_id
WHERE m.season='весна' AND c.name='Трубчатые' and r.size<6000





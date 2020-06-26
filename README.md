Problem Solving

docker run --publish=7474:7474 --publish=7687:7687 --env NEO4J_AUTH=neo4j/neo101 --volume=$HOME/neo4j/data:/Users/tahmid.tanzim/neo4j_data neo4j
neo101

1. CREATE (p:Person { name: "Emil", id: 123, cgpa: 3.99, is_active: true })
2. MATCH (p:Person) WHERE p.name = "Emil" RETURN p;
3. MATCH (ee:Person) WHERE ee.name = "Emil"
CREATE (js:Person { name: "Johan", from: "Sweden", learn: "surfing" }),
(ir:Person { name: "Ian", from: "England", title: "author" }),
(rvb:Person { name: "Rik", from: "Belgium", pet: "Orval" }),
(ally:Person { name: "Allison", from: "California", hobby: "surfing" }),
(ee)-[:KNOWS {since: 2001}]->(js),(ee)-[:KNOWS {rating: 5}]->(ir),
(js)-[:KNOWS]->(ir),(js)-[:KNOWS]->(rvb),
(ir)-[:KNOWS]->(js),(ir)-[:KNOWS]->(ally),
(rvb)-[:KNOWS]->(ally)
4. MATCH (ee:Person)-[:KNOWS]-(friends)
WHERE ee.name = "Emil" RETURN ee, friends
5. MATCH (js:Person)-[:KNOWS]-()-[:KNOWS]-(surfer)
WHERE js.name = "Johan" AND surfer.hobby = "surfing"
RETURN DISTINCT surfer
6. PROFILE MATCH (js:Person)-[:KNOWS]-()-[:KNOWS]-(surfer)
WHERE js.name = "Johan" AND surfer.hobby = "surfing"
RETURN DISTINCT surfer


docker run --rm -ti \
 --env-file <(env | grep -iE 'DEBUG|NODE_|ELECTRON_|YARN_|NPM_|CI|CIRCLE|TRAVIS_TAG|TRAVIS|TRAVIS_REPO_|TRAVIS_BUILD_|TRAVIS_BRANCH|TRAVIS_PULL_REQUEST_|APPVEYOR_|CSC_|GH_|GITHUB_|BT_|AWS_|STRIP|BUILD_') \
 --env ELECTRON_CACHE="/Users/tahmid.tanzim/.cache/electron" \
 --env ELECTRON_BUILDER_CACHE="/Users/tahmid.tanzim/.cache/electron-builder" \
 -v ${PWD}:/Users/tahmid.tanzim/Projects/one-eleven-desktop \
 -v ${PWD##*/}-node-modules:/Users/tahmid.tanzim/Projects/one-eleven-desktop/node_modules \
 -v ~/.cache/electron:/Users/tahmid.tanzim/.cache/electron \
 -v ~/.cache/electron-builder:/Users/tahmid.tanzim/.cache/electron-builder \
 electronuserland/builder:wine
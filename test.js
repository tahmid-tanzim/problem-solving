function anagrams() {

    let pendingInvitationList = [
        {
            "id": 237,
            "managerAccountId": 63,
            "managerName": "raffleshia aroni",
            "managerMobileNumber": "+8801800000000",
            "roleName": "Finance",
            "createdAt": 1512444101638,
            "profilePictures": [
                {
                    "url": "/image/02c451c2-a9d7-4a8c-a434-047525128144.jpg",
                    "quality": "high"
                },
                {
                    "url": "/image/c27dddb1-677e-420a-a78f-acf96a80b6db.jpg",
                    "quality": "medium"
                },
                {
                    "url": "/image/001afe6e-6243-4074-99b3-a64ad59c4019.jpg",
                    "quality": "low"
                }
            ]
        },
        {
            "id": 233,
            "managerAccountId": 288,
            "managerName": "Aditi",
            "managerMobileNumber": "+8801745017651",
            "roleName": "Finance",
            "createdAt": 1512384389931,
            "profilePictures": [
                {
                    "url": "/image/f0c7b4f7-4af0-48d7-9506-fcc961521e14.jpg",
                    "quality": "high"
                },
                {
                    "url": "/image/40929657-71f6-490d-8e60-faa7e42d24fc.jpg",
                    "quality": "medium"
                },
                {
                    "url": "/image/4435c4c4-f04f-4d95-a5fb-ade73444df73.jpg",
                    "quality": "low"
                }
            ]
        },
        {
            "id": 432,
            "managerAccountId": 130,
            "managerName": "Lupin",
            "managerMobileNumber": "+8801711643096",
            "roleName": "Admin",
            "createdAt": 1512384389931,
            "profilePictures": [
                {
                    "url": "/image/f0c7b4f7-4af0-48d7-9506-fcc961521e14.jpg",
                    "quality": "high"
                },
                {
                    "url": "/image/40929657-71f6-490d-8e60-faa7e42d24fc.jpg",
                    "quality": "medium"
                },
                {
                    "url": "/image/4435c4c4-f04f-4d95-a5fb-ade73444df73.jpg",
                    "quality": "low"
                }
            ]
        }
    ];

    const managerAccountId = 288;
    pendingInvitationList = pendingInvitationList.map(x => x.managerAccountId === managerAccountId ? Object.assign(x, {roleName: 'Super Admin'}) : x);

    console.log(JSON.stringify(pendingInvitationList, null, 2));
}

anagrams();
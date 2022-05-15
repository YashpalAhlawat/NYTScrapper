from scrapper.profile_scrapper import ProfileScrapper


class ProfileService:

    def fetch_profile_info(self):
        profile_scrapper = ProfileScrapper()
        data = profile_scrapper.execute()
        return data

if __name__ == "__main__":
    import argparse
    from content_filter import getAoaiResponse, getSecrets
    
    parser = argparse.ArgumentParser()
    parser.add_argument('region', help="Azure OpenAI service region")  #valid values EUS, EUS2, WUS, WUS3, NCUS
    parser.add_argument('api_ver', help="OpenAI API version") #2024-02-01
    parser.add_argument('prompt', help="Prompt to test for content filtration") # 'I love sushi! '; 'I am going to cut myself! '
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display filters",
    )
    args = parser.parse_args()
    
    region = args.region
    api_version = args.api_ver
    prompt = args.prompt
    
    key, endpoint = getSecrets(region.upper())
    resp = getAoaiResponse(prompt, key, endpoint, api_version)
    print(resp)
    
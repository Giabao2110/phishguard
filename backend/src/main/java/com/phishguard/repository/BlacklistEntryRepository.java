package com.phishguard.repository;

import com.phishguard.model.entity.BlacklistEntry;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BlacklistEntryRepository extends JpaRepository<BlacklistEntry, Long> {
    boolean existsByEntryValue(String entryValue);
}
